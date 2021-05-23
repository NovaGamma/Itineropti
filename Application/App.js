import React from "react";
import { StyleSheet, Text, View } from "react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import { List_of_adress } from "./component/List_adress";
import { Home } from "./component/Home";
import { Map } from "./component/Map";

function Old_destination({ navigation }) {
  return (
    <View>
      <Text style={{ textAlign: "center", fontSize: 24, fontWeight: "bold" }}>
        {" "}
        List of old destinations :{" "}
      </Text>
      <Text
        style={{
          textAlign: "center",
          alignSelf: "center",
          position: "absolute",
          top: 300,
        }}
      >
        Coming soon...
      </Text>
    </View>
  );
}

export default function App() {
  const Mystack = createStackNavigator();
  return (
    <NavigationContainer>
      <Mystack.Navigator initialRouteName="Home">
        <Mystack.Screen
          name="Home"
          component={Home}
          options={{
            headerShown: false,
          }}
        />
        <Mystack.Screen
          name="2ndPage"
          component={List_of_adress}
          options={{
            title: "Return to Home page",
          }}
        />
        <Mystack.Screen
          name="Mappage"
          component={Map}
          options={{
            title: "Return to Home page",
          }}
        />
        <Mystack.Screen
          name="Old_direction"
          component={Old_destination}
          options={{
            title: "Return to Home page",
          }}
        />
      </Mystack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({});
