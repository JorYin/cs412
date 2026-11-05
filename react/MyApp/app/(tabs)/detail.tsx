import { styles } from '../../assets/my_styles';

import { Image, ScrollView, StyleSheet } from 'react-native';
import { Text, View } from '@/components/Themed';

export default function DetailScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Some of my interests!</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <ScrollView>
        <Text style={[styles.title, detailStyles.text]}>Digital Art</Text>
        <Text style={[styles.description, detailStyles.text]}>
          I use digital tools to create illustrations, experiment with color,
          and bring creative ideas to life.
        </Text>
        <Image source={{ uri: 'https://cs-people.bu.edu/jordany/images/Digital_art.png' }} style={[styles.image, detailStyles.image]} accessibilityLabel="Digital art" />
        <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

        <Text style={[styles.title, detailStyles.text]}>Traditional Art</Text>
        <Text style={[styles.description, detailStyles.text]}>
          I enjoy drawing and painting by hand because they help me practice
          creativity and improve my artistic skills.
        </Text>
        <Image source={{ uri: 'https://cs-people.bu.edu/jordany/images/Traditional_art.png' }} style={[styles.image, detailStyles.image]} accessibilityLabel="Traditional art" />
        <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

        <Text style={[styles.title, detailStyles.text]}>PC Gaming</Text>
        <Text style={[styles.description, detailStyles.text]}>
          PC gaming is a fun way for me to relax, explore different worlds,
          and connect with other players.
        </Text>
        <Image source={{ uri: 'https://cs-people.bu.edu/jordany/images/gaming.png' }} style={[styles.image, detailStyles.image]} accessibilityLabel="PC gaming" />
        <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

        <Text style={[styles.title, detailStyles.text]}>PC Building</Text>
        <Text style={[styles.description, detailStyles.text]}>
          I enjoy choosing computer parts and assembling PCs that match
          different performance and budget needs.
        </Text>
        <Image source={{ uri: 'https://cs-people.bu.edu/jordany/images/pc_building.png' }} style={[styles.image, detailStyles.image]} accessibilityLabel="PC building" />
        <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

        <Text style={[styles.title, detailStyles.text]}>Coding</Text>
        <Text style={[styles.description, detailStyles.text]}>
          Coding allows me to solve problems, learn new technologies, and
          create useful applications.
        </Text>
        <Image source={{ uri: 'https://cs-people.bu.edu/jordany/images/coding.png' }} style={[styles.image, detailStyles.image]} accessibilityLabel="Coding" />
        <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

        <Text style={[styles.title, detailStyles.text]}>Photography</Text>
        <Text style={[styles.description, detailStyles.text]}>
          I like capturing interesting moments, places, and details through
          photographs.
        </Text>
        <Image source={{ uri: 'https://cs-people.bu.edu/jordany/images/photography.png' }} style={[styles.image, detailStyles.image]} accessibilityLabel="Photography" />
        <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

        <Text style={[styles.title, detailStyles.text]}>Small Business</Text>
        <Text style={[styles.description, detailStyles.text]}>
          I am interested in building a small business and learning how to
          turn creative ideas into products or services.
        </Text>
        <Image source={{ uri: 'https://cs-people.bu.edu/jordany/images/Business.png' }} style={[styles.image, detailStyles.image]} accessibilityLabel="Small business" />
        <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      </ScrollView>
    </View>
  );
}

const detailStyles = StyleSheet.create({
  text: {
    alignSelf: 'stretch',
    textAlign: 'left',
  },
  image: {
    alignSelf: 'center',
  },
});
