// File: feed.tsx
// Author: Jordan Yin
// Description: Display posts from profiles in the logged-in user's feed.

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

export default function FeedScreen() {
  const { token, profileId, authFetch } = useAuth();
  const [posts, setPosts] = useState<Post[]>([]);
  const [profiles, setProfiles] = useState<Profile[]>([]);
  const [isLoading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [error, setError] = useState('');

  async function loadFeed() {
    // A profile ID is required to request the current user's feed.
    if (!profileId) {
      return;
    }

    try {
      // authFetch includes the user's authentication token.
      // Load feed posts and profile details concurrently.
      const [feedResponse, profilesResponse] = await Promise.all([
        authFetch(
          `${API_BASE_URL}/mini_insta/api/profile/${profileId}/feed`,
        ),
        authFetch(`${API_BASE_URL}/mini_insta/api/profiles`),
      ]);

      // fetch only rejects network failures, so explicitly check HTTP status.
      if (!feedResponse.ok || !profilesResponse.ok) {
        throw new Error('Could not load the feed.');
      }

      // Parse the successful API responses into JavaScript data.
      const feedData = await feedResponse.json();
      const profilesData = await profilesResponse.json();

      // Save posts and profiles so the feed can display each post's author.
      setPosts(feedData.results ?? []);
      setProfiles(profilesData.results ?? profilesData);
    } catch (requestError) {
      // Save a readable error message for the error state in the UI.
      setError(
        requestError instanceof Error
          ? requestError.message
          : 'Could not load the feed.',
      );
    } finally {
      // Hide the loading indicator after either success or failure.
      setLoading(false);
    }
  }

  useEffect(() => {
    if (profileId && token) {
      setLoading(true);
      loadFeed();
    } else {
      setPosts([]);
      setProfiles([]);
      setLoading(true);
    }
  }, [token, profileId]);

  async function handleRefresh() {
    // Keep the pull-to-refresh indicator visible until the feed reloads.
    setRefreshing(true);
    await loadFeed();
    setRefreshing(false);
  }

  function getProfile(profileId: number) {
    return profiles.find((profile) => profile.id === profileId);
  }

  function formatTimestamp(timestamp: string) {
    return new Date(timestamp).toLocaleString();
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
        <FlatList
          data={posts}
          keyExtractor={(post) => post.id.toString()}
          contentContainerStyle={styles.feedContainer}
          refreshing={refreshing}
          onRefresh={handleRefresh}
          renderItem={({ item }) => {
            const postProfile = getProfile(item.profile_id);

            return (
              <View style={styles.feedPost}>
                <View style={styles.feedPostHeader}>
                  {postProfile?.profile_image_url ? (
                    <Image
                      source={{ uri: postProfile.profile_image_url }}
                      style={styles.feedProfileImage}
                    />
                  ) : (
                    <View style={styles.feedProfileImagePlaceholder} />
                  )}

                  <View style={styles.feedPostHeaderText}>
                    <Text style={styles.feedUsername}>
                      {postProfile?.username ?? 'Unknown profile'}
                    </Text>
                    <Text style={styles.feedTimestamp}>
                      {formatTimestamp(item.timestamp)}
                    </Text>
                  </View>
                </View>

                {item.photos[0] ? (
                  <Image
                    source={{ uri: item.photos[0].image }}
                    style={styles.feedPostImage}
                  />
                ) : (
                  <Image
                    source={{ uri: FALLBACK_IMAGE }}
                    style={styles.feedPostImage}
                  />
                )}

                {item.caption ? (
                  <Text style={styles.feedCaption}>{item.caption}</Text>
                ) : null}
              </View>
            );
          }}
        />
      )}
    </View>
  );
}
