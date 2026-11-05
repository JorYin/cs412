import { styles } from '../../assets/my_styles';

import { Image } from 'react-native';
import { Text, View } from '@/components/Themed';

export default function AboutScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>About</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <Text style={styles.description}>
        I am a creative and curious person who enjoys combining art,
        technology, and entrepreneurship. My interests include digital and
        traditional art, PC gaming and building, coding, photography, and
        growing a small business.
      </Text>
      <Image
        source={require('../../assets/images/icon.png')}
        style={styles.image}
        accessibilityLabel="My project icon"
      />
    </View>
  );
}
