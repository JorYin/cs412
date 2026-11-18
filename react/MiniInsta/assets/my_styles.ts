import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  container: {
    paddingHorizontal: 16,
    paddingTop: 16,
    paddingBottom: 32,
  },
  centered: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
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
  profileHeader: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    width: '100%',
    marginBottom: 20,
  },
  profileImage: {
    width: 96,
    height: 96,
    borderRadius: 48,
    marginRight: 16,
  },
  profileImagePlaceholder: {
    width: 96,
    height: 96,
    borderRadius: 48,
    marginRight: 16,
    backgroundColor: '#ddd',
  },
  profileDetails: {
    flex: 1,
    paddingTop: 2,
  },
  username: {
    fontSize: 22,
    fontWeight: 'bold',
  },
  displayName: {
    fontSize: 16,
    marginTop: 2,
  },
  postCount: {
    fontSize: 15,
    fontWeight: '600',
    marginTop: 8,
  },
  bio: {
    fontSize: 15,
    marginTop: 6,
  },
  postGridRow: {
    justifyContent: 'space-between',
    marginBottom: 12,
  },
  postGridItem: {
    width: '31.5%',
  },
  postImage: {
    width: '100%',
    aspectRatio: 1,
    borderRadius: 12,
  },
  postImagePlaceholder: {
    backgroundColor: '#eee',
  },
});

export default styles