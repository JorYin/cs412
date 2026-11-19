// File: AuthContext.tsx
// Author: Jordan Yin (jordany@bu.edu), 11/19/2026
// Description: Authentication state, token persistence, login, logout, and authenticated requests.

import {
  createContext,
  type ReactNode,
  useContext,
  useEffect,
  useState,
} from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';

const AuthContext = createContext<any>(null);

export function useAuth() {
  // Retrieve the authentication values and actions from the provider.
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error('useAuth must be used inside AuthProvider');
  }

  return context;
}

export function AuthProvider({ children }: { children: ReactNode }) {
  // Store the logged-in token and profile ID in React state.
  const [token, setToken] = useState<string | null>(null);
  const [profileId, setProfileId] = useState<string | null>(null);
  
  useEffect(() => {
    // Restore the saved authentication session when the app launches.
    (async () => {
      setToken(await AsyncStorage.getItem('auth_token'));
      setProfileId(await AsyncStorage.getItem('profile_id'));
    })();
  }, []);
  
  const login = async (username, password) => {
    // Send credentials to Django and receive a token and profile.
    const response = await fetch(
      'https://cs-webapps.bu.edu/jordany/mini_insta/api/login/',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      },
    );

    if (!response.ok) {
      throw new Error('Invalid username or password.');
    }

    const data = await response.json();
    const profileId = data.profile.id.toString();

    await AsyncStorage.setItem('auth_token', data.token);
    await AsyncStorage.setItem('profile_id', profileId);

    setToken(data.token);
    setProfileId(profileId);
  };
  
  const logout = async () => {
    // Remove saved credentials and clear the React authentication state.
    await AsyncStorage.removeItem('auth_token');
    await AsyncStorage.removeItem('profile_id');
    setToken(null);
    setProfileId(null);
  };
  
  const authFetch = async (url, options = {}) => {
    // Attach the token to protected API requests.
    const res = await fetch(url, { ...options, headers: {
      ...options.headers, Authorization: `Token ${token}` } });
    // Clear stale authentication when Django rejects the token.
    if (res.status === 401) await logout();
    return res;
  };
  
  return <AuthContext.Provider value={{ token, profileId, login, logout, authFetch }}>{children}
  </AuthContext.Provider>;
}