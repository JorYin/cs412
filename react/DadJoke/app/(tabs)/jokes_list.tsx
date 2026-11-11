import { styles } from '../../assets/my_styles';

import { ActivityIndicator, FlatList } from 'react-native';
import { Text, View } from '@/components/Themed';
import { useState, useEffect } from 'react';

export default function JokeListScreen() {
  const jokeListAPI = 'https://cs-webapps.bu.edu/jordany/dadjokes/api/jokes';
  const [jokeList, setJokeList] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);

  const fetchJokeList = async () => {
    try {
      const response = await fetch(jokeListAPI);
      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }

      const data = await response.json();
      setJokeList(data.results);
    } catch (error) {
      console.error('Unable to load jokes:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleRefresh = () => {
    setRefreshing(true);
    fetchJokeList();
    setRefreshing(false);
  }

  useEffect(() => {
    fetchJokeList();
  }, []);

  return (
    <View style={styles.container}>
      {isLoading ? (
        <ActivityIndicator size="large" />
      ) : (
        <FlatList
          data={jokeList}
          renderItem={({ item }) => (
            <View style={styles.container}>
              <Text style={styles.title}>{item.joke}</Text>
              <Text style={styles.description}>By: {item.contributor}</Text>
            </View>
          )}
          refreshing ={refreshing}
          onRefresh={handleRefresh}
        />
      )}
    </View>
  );
}
