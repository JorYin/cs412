import { Image } from 'react-native';
import { styles } from '../../assets/my_styles';

import { Text, View } from '@/components/Themed';

export default function IndexScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to My Index Page</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <Text style={styles.description}>
        This is my initial index page. To learn more about me please look at the details page for some hobbies I enjoy. Then to learn more about me look towards the about page! Have fun!!!
      </Text>
      <Image
        source={require('../../assets/images/android-icon-foreground.png')}
        style={styles.image}
        accessibilityLabel="Image of myself"
      />
    </View>
  );
}
