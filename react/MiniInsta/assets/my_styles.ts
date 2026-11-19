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
  label: {
    alignSelf: 'stretch',
    fontSize: 16,
    fontWeight: '600',
    marginBottom: 8,
  },
  captionInput: {
    alignSelf: 'stretch',
    borderColor: '#999',
    borderRadius: 8,
    borderWidth: 1,
    minHeight: 100,
    padding: 12,
    marginBottom: 20,
  },
  imageUrlsInput: {
    alignSelf: 'stretch',
    borderColor: '#999',
    borderRadius: 8,
    borderWidth: 1,
    minHeight: 80,
    padding: 12,
    marginBottom: 16,
  },
  createPostMessage: {
    alignSelf: 'stretch',
    marginBottom: 16,
  },
  createPostButton: {
    alignSelf: 'stretch',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#2f95dc',
    borderRadius: 8,
    minHeight: 48,
  },
  createPostButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  feedContainer: {
    paddingHorizontal: 16,
    paddingTop: 16,
    paddingBottom: 32,
  },
  feedPost: {
    marginBottom: 28,
  },
  feedPostHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 12,
  },
  feedProfileImage: {
    width: 44,
    height: 44,
    borderRadius: 22,
    marginRight: 10,
  },
  feedProfileImagePlaceholder: {
    width: 44,
    height: 44,
    borderRadius: 22,
    marginRight: 10,
    backgroundColor: '#ddd',
  },
  feedPostHeaderText: {
    flex: 1,
  },
  feedUsername: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  feedTimestamp: {
    fontSize: 13,
    marginTop: 2,
  },
  feedPostImage: {
    width: '100%',
    aspectRatio: 1,
    borderRadius: 12,
  },
  feedCaption: {
    fontSize: 16,
    marginTop: 12,
  },
  loginContainer: {
    flex: 1,
    justifyContent: 'center',
    paddingHorizontal: 24,
  },
  loginTitle: {
    fontSize: 32,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 32,
  },
  loginMessage: {
    textAlign: 'center',
    marginBottom: 16,
  },
  loginInput: {
    borderColor: '#999',
    borderRadius: 8,
    borderWidth: 1,
    fontSize: 16,
    marginBottom: 12,
    paddingHorizontal: 12,
    minHeight: 48,
  },
  loginButton: {
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#2f95dc',
    borderRadius: 8,
    minHeight: 48,
  },
  loginButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});

export default styles