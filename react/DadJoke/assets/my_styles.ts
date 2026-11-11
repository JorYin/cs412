import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  description: {
    fontSize: 16,
    lineHeight: 24,
    marginBottom: 24,
    textAlign: 'center',
  },
  input: {
    alignSelf: 'stretch',
    borderColor: '#999',
    borderRadius: 8,
    borderWidth: 1,
    fontSize: 16,
    marginBottom: 16,
    minHeight: 48,
    padding: 12,
  },
  image: {
    height: 200,
    width: 200,
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});

export default styles