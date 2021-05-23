import React, { useState } from "react";
import { View, StyleSheet, TouchableOpacity, Image } from "react-native";
import Constants from "expo-constants";
import Panda from "./Panda";
import List_of_adress from "./List_adress";

export function Map({ route, navigation }) {
  const tempTravel = route.params.adresses;

  const [isVisible, setVisibility] = useState(true);

  const onSwitchVisibility = () => {
    navigation.navigate({
      name: "2ndPage",
      params: {},
    });
  };

  return (
    <View style={styles.container}>
      {isVisible && <Panda stepList={tempTravel} />}
      <TouchableOpacity
        style={styles.switchButton}
        onPress={onSwitchVisibility}
      >
        <Image
          source={
            isVisible
              ? require("../assets/menu.png")
              : require("../assets/map.png")
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
    justifyContent: "center",
    paddingTop: Constants.statusBarHeight,
    backgroundColor: "#ecf0f1",
    padding: 8,
  },
  switchButton: {
    position: "absolute",
    top: 30,
    left: 15,
    width: 50,
    height: 50,
  },
  btnImage: {
    width: 50,
    height: 50,
  },
});
