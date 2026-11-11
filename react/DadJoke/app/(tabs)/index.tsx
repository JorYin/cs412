import { ActivityIndicator, Button, Image } from 'react-native';
import { styles } from '../../assets/my_styles';
import { Text, View } from '@/components/Themed';
import { useState, useEffect } from 'react';

type Joke = {
  joke: string;
  contributor: string;
};

export default function IndexScreen() {
  const jokeAPI = 'https://cs-webapps.bu.edu/jordany/dadjokes/api/random';
  const pictureAPI = 'https://cs-webapps.bu.edu/jordany/dadjokes/api/random_picture';

  const [joke, setJoke] = useState<Joke | null>(null);
  const [picture, setPicture] = useState('');
  const [isLoading, setIsLoading] = useState(true);

  const fetchPicture = async () => {
    try {
      const response = await fetch(pictureAPI);

      const data = await response.json();
      setPicture(data.image_url);
    } catch (error) {
      console.error('Unable to load picture:', error);
      setPicture('');
    }
  };

  const fetchJoke = async () => {
    try {
      const response = await fetch(jokeAPI);

      const data = await response.json();
      setJoke(data);
    } catch (error) {
      console.error('Unable to load joke:', error);
      setJoke(null);
    }
  };

  const loadContent = async () => {
    setIsLoading(true);
    fetchJoke();
    fetchPicture();
    setIsLoading(false);
  };

  useEffect(() => {
    loadContent();
  }, []);

  return (
    <View style={styles.container}>
      {isLoading ? (
        <ActivityIndicator size="large" />
      ) : (
        <>
          <Image source={{ uri: picture }} style={styles.image} />
          <Text style={styles.title}>{joke.joke}</Text>
          <Text style={styles.description}>By {joke.contributor}</Text>
        </>
      )}
      <Button
        title={isLoading ? 'Loading...' : 'New Joke'}
        color="#007AFF"
        onPress={loadContent}
        disabled={isLoading}
      />
    </View>
  );
}
