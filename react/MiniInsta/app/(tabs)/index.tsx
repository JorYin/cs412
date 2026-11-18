import { useEffect, useState } from 'react';
import {
  ActivityIndicator,
  FlatList,
  Image,
  Text,
  View,
} from 'react-native';
import styles from '@/assets/my_styles';
import type { Post, Profile } from '@/types/MiniInstaTypes';

const API_BASE_URL = 'https://cs-webapps.bu.edu/jordany';
const PROFILE_ID = 1;

export default function ProfileScreen() {
  const [profile, setProfile] = useState<Profile | null>(null);
  const [posts, setPosts] = useState<Post[]>([]);
  const [isLoading, setLoading] = useState(true);
  const [error, setError] = useState('');

  async function loadProfileData() {
    try {
      const [profileResponse, postsResponse] = await Promise.all([
        fetch(`${API_BASE_URL}/mini_insta/api/profile/${PROFILE_ID}`),
        fetch(`${API_BASE_URL}/mini_insta/api/profile/${PROFILE_ID}/posts`),
      ]);

      if (!profileResponse.ok || !postsResponse.ok) {
        throw new Error('Could not load profile data.');
      }

      const profileData = await profileResponse.json();
      const postsData = await postsResponse.json();

      setProfile(profileData);
      setPosts(postsData.results ?? []);
    } catch (requestError) {
      setError(
        requestError instanceof Error
          ? requestError.message
          : 'Could not load profile data.',
      );
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadProfileData();
  }, []);

  if (error) {
    return (
      <View style={styles.centered}>
        <Text>{error}</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      {isLoading ? (
        <ActivityIndicator size="large" />
      ) : (
        <>
          {profile ? (
            <View style={styles.profileHeader}>
              {profile.profile_image_url ? (
                <Image
                  source={{ uri: profile.profile_image_url }}
                  style={styles.profileImage}
                />
              ) : (
                <View style={styles.profileImagePlaceholder} />
              )}

              <View style={styles.profileDetails}>
                <Text style={styles.username}>{profile.username}</Text>
                <Text style={styles.displayName}>{profile.display_name}</Text>
                <Text style={styles.postCount}>{profile.post_count} Posts</Text>
                <Text style={styles.bio}>{profile.bio_text}</Text>
              </View>
            </View>
          ) : null}

          <FlatList
            key="profile-post-grid"
            data={posts}
            keyExtractor={(post) => post.id.toString()}
            numColumns={3}
            columnWrapperStyle={styles.postGridRow}
            renderItem={({ item }) => (
              <View style={styles.postGridItem}>
                {item.photos[0] ? (
                  <Image
                    source={{
                      uri: item.photos[0].image,
                    }}
                    style={styles.postImage}
                  />
                ) : (
                  <Image
                    source={{
                      uri: 'https://img.magnific.com/premium-vector/letter-x-dry-brush-stroke-typography-vector_53876-177859.jpg',
                    }}
                    style={styles.postImage}
                  />
                )}
              </View>
            )}
          />
        </>
      )}
    </View>
  );
}
