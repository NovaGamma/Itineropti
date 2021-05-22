import React from 'react';
import {StyleSheet, View, Dimensions, Text} from 'react-native';
import MapView, {Marker} from 'react-native-maps';
import MapViewDirections from 'react-native-maps-directions';
import {GOOGLE_API_KEY} from "./constants";

export default function Panda(props) {

  const stepList = props.stepList;
  let stepPair = [];
  let origin = {
    latitude: 0,
    longitude: 0,
  }

  if (stepList.length == 1){
    stepPair.push({
      origin:stepList[0],
      destination:stepList[0],
    })
    origin = stepPair[0].origin;
  }
  
  if (stepList.length > 2){
    for (let i = 1; i < stepList.length; i++){
      stepPair.push({
        origin:stepList[i-1],
        destination:stepList[i],
      });
    }
    origin = stepPair[0].origin;
  }

  return (
    <View style={styles.container}>
      <MapView
        style={styles.maps}
        initialRegion={{
          latitude:origin.latitude,
          longitude: origin.longitude,
          latitudeDelta: 0.0622,
          longitudeDelta: 0.0121,
        }}>
        { !!stepList.length && <Marker coordinate={stepPair[0].origin}/> }
        {stepPair.map((item) => {
          return(
            <View>
              <MapViewDirections
                origin={item.origin}
                destination={item.destination}
                apikey={GOOGLE_API_KEY}
                strokeWidth={4}
                strokeColor="#111111"
              />
              <Marker coordinate={item.destination} />
            </View>
          );
        })}
      </MapView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  maps: {
    width: Dimensions.get('screen').width,
    height: Dimensions.get('screen').height,
  },
});