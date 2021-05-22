import React, {useState} from 'react';
import { Text, View, StyleSheet, TouchableOpacity, Image } from 'react-native';
import Constants from 'expo-constants';
import Panda from './components/Panda';
import RedPanda from './components/RedPanda';

export default function App() {
  const tempTravel = [
        {
          latitude: 48.8587741,
          longitude: 2.2069771,
        },
        {
          latitude: 48.8323785,
          longitude: 2.3361663,
        },
        {
          latitude: 48.83,
          longitude: 2.33,
        }
      ];
  
  const [isVisible, setVisibility] = useState(true);
  
  const onSwitchVisibility = () => {
    setVisibility(!isVisible);
  }


  return (
    <View style={styles.container}>
      { isVisible && <Panda stepList = {tempTravel}/>}
      { !isVisible && <RedPanda />}
      <TouchableOpacity style={styles.switchButton} onPress={onSwitchVisibility}>
        <Image 
          source={
            isVisible?
              require('./assets/menu.png')
            :
              require('./assets/map.png')
            }
          style={styles.btnImage}
        />
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    paddingTop: Constants.statusBarHeight,
    backgroundColor: '#ecf0f1',
    padding: 8,
  },
  switchButton: {
    position: "absolute",
    bottom: 30,
    left: 15,
    width: 50,
    height: 50
  },
  btnImage: {
    width: 50,
    height: 50
  }
});
