import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  Platform,
  TextInput,
  KeyboardAvoidingView,
  TouchableOpacity,
  Keyboard,
  Image,
} from "react-native";

import Adress from "./Adress";

export function List_of_adress({ route, navigation }) {
  const [adress, setAdress] = useState();

  const handleAddAdress = () => {
    if (adress === null || adress.length < 5) {
      //check validity of adress
      alert("This adress is too short!");
    } else {
      Keyboard.dismiss(); //removes keyboardtask
      setAdressItems([...adressItems, adress]); //whatever was already in adressItems we add an adress
      setAdress("");
    }
  };
  const [adressItems, setAdressItems] = useState([]);

  const submit_adress = async () => {
    let url = "https://itineroptiapp.herokuapp.com/address/";
    if (adressItems.length > 0) {
      for (var i = 0; i < adressItems.length; i++) {
        url = url + adressItems[i] + "|";
      }
      url = url.slice(0, url.length - 1);
      try {
        let response = await fetch(url);
        let test = await response.json();
        return test;
      } catch (error) {
        console.log(error);
      }
    }
  };

  const clear = () => {
    setAdressItems([]);
  };

  const removeAdress = (index) => {
    let itemsCopy = [...adressItems];
    itemsCopy.splice(index, 1);
    setAdressItems(itemsCopy);
  };

  const GetAdress = async () => {
    let getadress = await submit_adress();
    navigation.navigate({
      name: "Mappage",
      params: { adresses: getadress },
    });
  };

  return (
    <View style={styles.container}>
      <View style={styles.adressWrapper}>
        <View
          style={{
            alignItems: "center",
            justifyContent: "space-around",
            flexDirection: "row",
          }}
        >
          {/*clear button*/}
          <TouchableOpacity style={styles.clearButton} onPress={() => clear()}>
            <Text>CLEAR</Text>
          </TouchableOpacity>

          {/*Title*/}
          <Text style={styles.SectionTitle}>Adresses!</Text>

          {/*Submit*/}
          <TouchableOpacity
            style={styles.submitButton}
            onPress={() => GetAdress()}
          >
            <Text>SUBMIT</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.items}>
          {adressItems.map((item, index) => {
            //used to loop through a list
            return (
              <View style={{ padding: 2 }}>
                <Adress text={item} key={index} />
                <TouchableOpacity
                  style={styles.touchable}
                  onPress={() => removeAdress(index)}
                >
                  <Image
                    style={styles.trash}
                    source={require("../assets/trash.png")}
                  />
                </TouchableOpacity>
              </View>
            );
          })}
        </View>
      </View>

      {/*write an adress*/}
      <KeyboardAvoidingView //everything goes up as the keyboard pops up
        behavior={Platform.OS === "ios" ? "padding" : "height"}
        style={styles.writeAdressWrapper}
      >
        <TextInput
          style={styles.input}
          placeholder={"Enter Adress"}
          value={adress}
          onChangeText={(text) => setAdress(text)}
        />

        <TouchableOpacity onPress={() => handleAddAdress()}>
          <View style={styles.addWrapper}>
            <Text style={styles.addText}>+</Text>
          </View>
        </TouchableOpacity>
      </KeyboardAvoidingView>
    </View>
  );
}

const styles = StyleSheet.create({
  //returns a container object, stylesheet.create is to give us an error
  container: {
    flex: 1,
    backgroundColor: "#FCBABA",
  },
  adressWrapper: {
    paddingTop: 80,
    paddingHorizontal: 20,
  },
  SectionTitle: {
    fontSize: 24,
    fontWeight: "bold",
    textAlign: "center",
  },
  items: {
    marginTop: 30,
  },
  writeAdressWrapper: {
    position: "absolute",
    bottom: 10,
    width: "100%",
    flexDirection: "row",
    justifyContent: "space-around",
    alignItems: "center",
  },
  input: {
    paddingVertical: 15,
    paddingHorizontal: 15,
    backgroundColor: "#E4F2D5",
    borderRadius: 60,
    borderColor: "black",
    borderWidth: 2,
    width: 250,
  },
  addWrapper: {
    width: 60,
    height: 60,
    backgroundColor: "#E4F2D5",
    borderRadius: 60,
    borderColor: "black",
    borderWidth: 2,
    justifyContent: "center",
    alignItems: "center",
  },
  trash: {
    width: 25,
    height: 25,
  },
  touchable: {
    zIndex: 2,
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    position: "absolute",
    marginTop: 12,
    marginLeft: 10,
  },

  clearButton: {
    width: "25%",
    height: "75%",
    borderWidth: 2,
    alignItems: "center",
    backgroundColor: "#F72427",
    borderRadius: 3,
  },
  submitButton: {
    width: "25%",
    height: "75%",
    borderWidth: 2,
    alignItems: "center",
    backgroundColor: "#67DC19",
    borderRadius: 3,
  },
});
