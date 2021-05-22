import React from 'react';
import {StyleSheet, View, Dimensions, Text} from 'react-native';

export default function RedPanda() {
  return (
    <View style={styles.container}>
      <Text style={styles.ll}>Panda is life Red Panda is love</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent:"center",
    alignItems:"center"
  },
  ll:{
    fontSize:25
  }
});