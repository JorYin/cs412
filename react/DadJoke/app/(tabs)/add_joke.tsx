import { styles } from '../../assets/my_styles';

import { useState } from 'react';
import { Alert, Button, TextInput } from 'react-native';
import { Text, View } from '@/components/Themed';

export default function AddJokeScreen() {
  const jokePOSTAPI = 'https://cs-webapps.bu.edu/jordany/dadjokes/api/jokes';
  const [joke, setJoke] = useState('');
  const [contributor, setContributor] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const submitJoke = async () => {
    const trimmedJoke = joke.trim();
    const trimmedContributor = contributor.trim();

    setIsLoading(true);
    console.log('Submitting joke to Django API:', {
      joke: trimmedJoke,
      contributor: trimmedContributor,
    });

    try {
      const response = await fetch(jokePOSTAPI, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          joke: trimmedJoke,
          contributor: trimmedContributor,
        }),
      });

      console.log('Django API response status:', response.status);

      setJoke('');
      setContributor('');
      Alert.alert('Joke added', 'Your joke was submitted successfully.');
    } catch (error) {
      console.error('Unable to submit joke:', error);
      Alert.alert('Submission failed', 'The joke could not be submitted. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Add a Joke</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter a joke"
        placeholderTextColor="#777"
        multiline
        value={joke}
        onChangeText={setJoke}
        editable={!isLoading}
      />
      <TextInput
        style={styles.input}
        placeholder="Your name"
        placeholderTextColor="#777"
        value={contributor}
        onChangeText={setContributor}
        editable={!isLoading}
      />
      <Button
        title={isLoading ? 'Submitting...' : 'Submit Joke'}
        onPress={submitJoke}
        disabled={isLoading}
      />
    </View>
  );
}
