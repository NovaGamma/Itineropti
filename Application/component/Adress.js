import React from "react";
import { View, Text, StyleSheet, TouchableOpacity, Image } from "react-native";

const Adress = (props) => {
  return (
    <View style={styles.item}>
      <Text numberOfLines={1} style={{ marginLeft: 25, fontSize: 17 }}>
        {props.text}
      </Text>
    </View>
  );
};

const styles = StyleSheet.create({
  item: {
    backgroundColor: "#E4F2D5",
    borderColor: "black",
    borderWidth: 2,
    padding: 10,
    borderRadius: 10,
    alignItems: "center",
    justifyContent: "space-between", //for trash can to be at the end
    position: "relative",
    zIndex: 1,
    flexDirection: "row",
  },
});

export default Adress;
