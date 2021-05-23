import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableHighlight,
} from "react-native";

export function Home({ route, navigation }) {
  return (
    <View style={styles.container}>
      <Image style={styles.logo} source={require("../assets/logo.png")} />
      <Text style={styles.text_logo}>Itineropti</Text>
      <View style={styles.buttons_style}>
        <TouchableHighlight onPress={() => navigation.navigate("2ndPage")}>
          <View style={styles.homebuttons}>
            <Text style={styles.hometext}>New direction</Text>
          </View>
        </TouchableHighlight>
        <View style={{ height: 20 }} />
        <TouchableHighlight
          onPress={() => navigation.navigate("Old_direction")}
        >
          <View style={styles.homebuttons}>
            <Text style={styles.hometext}>Old direction</Text>
          </View>
        </TouchableHighlight>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#8FE381",
    alignItems: "center",
    justifyContent: "center",
  },
  logo: {
    height: "12%",
    width: "20%",
    position: "absolute",
    top: 20,
  },
  text_logo: {
    fontSize: 30,
    position: "absolute",
    top: 110,
    textAlign: "center",
    fontWeight: "bold",
    color: "#DE2514",
  },
  buttons_style: {
    flex: 1,
    justifyContent: "center",
  },
  homebuttons: {
    width: 200,
    height: 75,
    justifyContent: "center",
    backgroundColor: "#E34234",
    borderRadius: 10,
  },
  hometext: {
    fontWeight: "bold",
    color: "white",
    fontSize: 20,
    textAlign: "center",
  },
});
