import { StyleSheet, Text, View } from 'react-native';

export default function CreatePostScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Create Post</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
  },
});
