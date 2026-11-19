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

export default function LoginScreen() {
  const { token, profileId, login, logout } = useAuth();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setLoading] = useState(false);
  const [message, setMessage] = useState('');

  async function handleLogin() {
    setLoading(true);
    setMessage('');

    try {
      await login(username, password);
      setMessage('Login successful.');
    } catch (requestError) {
      setMessage(
        requestError instanceof Error
          ? requestError.message
          : 'Could not log in.',
      );
    } finally {
      setLoading(false);
    }
  }

  if (token) {
    return (
      <View style={styles.loginContainer}>
        <Text style={styles.loginTitle}>Logged In</Text>
        <Text style={styles.loginMessage}>Profile ID: {profileId}</Text>
        <Pressable style={styles.loginButton} onPress={logout}>
          <Text style={styles.loginButtonText}>Log Out</Text>
        </Pressable>
      </View>
    );
  }

  return (
    <View style={styles.loginContainer}>
      <Text style={styles.loginTitle}>Login</Text>

      <TextInput
        value={username}
        onChangeText={setUsername}
        style={styles.loginInput}
        autoCapitalize="none"
        placeholder="Username"
      />

      <TextInput
        value={password}
        onChangeText={setPassword}
        style={styles.loginInput}
        secureTextEntry
        placeholder="Password"
      />

      {message ? (
        <Text style={styles.loginMessage}>{message}</Text>
      ) : null}

      <Pressable
        style={styles.loginButton}
        onPress={handleLogin}
        disabled={isLoading}
      >
        {isLoading ? (
          <ActivityIndicator color="#fff" />
        ) : (
          <Text style={styles.loginButtonText}>Log In</Text>
        )}
      </Pressable>
    </View>
  );
}
