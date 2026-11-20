// File: index.tsx
// Author: Jordan Yin
// Description: Display the logged-in user's profile and posts.

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
import {
  API_BASE_URL,
  FALLBACK_IMAGE,
} from '@/types/MiniInstaTypes';
import { useAuth } from '@/context/AuthContext';

export default function ProfileScreen() {
  const { token, profileId, authFetch } = useAuth();
  const [profile, setProfile] = useState<Profile | null>(null);
  const [posts, setPosts] = useState<Post[]>([]);
  const [isLoading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [error, setError] = useState('');

  async function loadProfileData() {
    // A profile ID is required to build the profile API URLs.
    if (!profileId) {
      return;
    }

    try {
      // authFetch adds the user's authentication token to each request.
      // Promise.all loads the profile and posts at the same time.
      const [profileResponse, postsResponse] = await Promise.all([
        authFetch(`${API_BASE_URL}/mini_insta/api/profile/${profileId}`),
        authFetch(`${API_BASE_URL}/mini_insta/api/profile/${profileId}/posts`),
      ]);

      // fetch does not reject for HTTP errors, so check both responses manually.
      if (!profileResponse.ok || !postsResponse.ok) {
        throw new Error('Could not load profile data.');
      }

      // Convert both successful response bodies from JSON into JavaScript data.
      const profileData = await profileResponse.json();
      const postsData = await postsResponse.json();

      // Store the API data so React can render the profile and post grid.
      setProfile(profileData);
      setPosts(postsData.results ?? []);
    } catch (requestError) {
      // Save a readable error message for the error state in the UI.
      setError(
        requestError instanceof Error
          ? requestError.message
          : 'Could not load profile data.',
      );
    } finally {
      // Hide the loading indicator after either success or failure.
      setLoading(false);
    }
  }

  useEffect(() => {
    if (profileId && token) {
      setLoading(true);
      loadProfileData();
    } else {
      setProfile(null);
      setPosts([]);
      setLoading(true);
    }
  }, [token, profileId]);

  async function handleRefresh() {
    // Keep the pull-to-refresh indicator visible until the request finishes.
    setRefreshing(true);
    await loadProfileData();
    setRefreshing(false);
  }

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
            refreshing={refreshing}
            onRefresh={handleRefresh}
            renderItem={({ item }) => (
              <View style={styles.postGridItem}>
                {item.photos[0] ? (
                  <Image
                    source={{
                      uri: item.photos[0].image.startsWith('http')
                        ? item.photos[0].image
                        : `${API_BASE_URL}${item.photos[0].image}`,
                    }}
                    style={styles.postImage}
                  />
                ) : (
                  <Image
                    source={{
                      uri: FALLBACK_IMAGE,
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
