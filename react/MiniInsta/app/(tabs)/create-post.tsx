// File: create-post.tsx
// Author: Jordan Yin
// Description: Collect and submit a new MiniInsta post.

import { useState } from 'react';
import {
  ActivityIndicator,
  Pressable,
  Text,
  TextInput,
  View,
} from 'react-native';
import styles from '@/assets/my_styles';
import { useAuth } from '@/context/AuthContext';
import {
  API_BASE_URL,
} from '@/types/MiniInstaTypes';

export default function CreatePostScreen() {
  const { token, authFetch, profileId } = useAuth();
  const [caption, setCaption] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  const [isLoading, setLoading] = useState(false);
  const [message, setMessage] = useState('');

  async function createPost() {
    if (!profileId) {
      setMessage('Waiting for profile information.');
      return;
    }

    setLoading(true);
    setMessage('');

    const imageUrlList = imageUrl.trim()
      ? [imageUrl.trim()]
      : [];

    try {
      const response = await authFetch(
        `${API_BASE_URL}/mini_insta/api/posts`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            caption,
            image_urls: imageUrlList,
          }),
        },
      );

      if (!response.ok) {
        throw new Error('Could not create the post.');
      }

      setCaption('');
      setImageUrl('');
      setMessage('Post created successfully.');
    } catch (requestError) {
      setMessage(
        requestError instanceof Error
          ? requestError.message
          : 'Could not create the post.',
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Create Post</Text>

      {!profileId || !token ? (
        <ActivityIndicator size="large" />
      ) : (
        <>
          <Text style={styles.label}>Caption</Text>
          <TextInput
            value={caption}
            onChangeText={setCaption}
            style={styles.captionInput}
            multiline
            placeholder="Write a caption"
          />

          <Text style={styles.label}>Image URL</Text>
          <TextInput
            value={imageUrl}
            onChangeText={setImageUrl}
            style={styles.imageUrlsInput}
            multiline
            autoCapitalize="none"
            placeholder="https://example.com/photo1.jpg"
          />

          {message ? (
            <Text style={styles.createPostMessage}>{message}</Text>
          ) : null}

          <Pressable
            style={styles.createPostButton}
            onPress={createPost}
            disabled={isLoading || !profileId}
          >
            {isLoading ? (
              <ActivityIndicator color="#fff" />
            ) : (
              <Text style={styles.createPostButtonText}>Create Post</Text>
            )}
          </Pressable>
        </>
      )}
    </View>
  );
}
