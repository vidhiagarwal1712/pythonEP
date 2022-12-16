import * as React from 'react';
import {
  Text,
  View,
  StyleSheet,
  TextInput,
  Image,
  TouchableOpacity,
} from 'react-native';
import Constants from 'expo-constants';
import DropdownPicker from 'react-native-dropdown-picker';
import db from '../config.js';
import firebase from 'firebase';

export default class Writestory extends React.Component {
  constructor() {
    super();
    this.state = {
      title: '',
      author: firebase
        .auth()
        .currentUser.email.substring(
          0,
          firebase.auth().currentUser.email.indexOf('@')
        ),
      description: '',
      moral: '',
      story:'',
      fileimage: '',
    };
  }
  addstory = () => {
    db.collection('stories').add({
      title: this.state.title,
      author: this.state.author,
      description: this.state.description,
      moral: this.state.moral,
      story:this.state.story,
      created_on: firebase.firestore.Timestamp.now().toDate().toString(),
      image: this.state.fileimage
    });
  };
  render() {
    let allimages = {
      image1: require('../assets/story_image_1.png'),
      image2: require('../assets/story_image_2.png'),
      image3: require('../assets/story_image_3.png'),
      image4: require('../assets/story_image_4.png'),
    };
    return (
      <View style={styles.container}>
        <Text style={styles.header}>Storytelling App</Text>
        <Image
          source={allimages[this.state.fileimage]}
          style={styles.displayimage}></Image>
        <DropdownPicker
          items={[
            { label: 'IMAGE1', value: 'image1' },
            { label: 'IMAGE2', value: 'image2' },
            { label: 'IMAGE3', value: 'image3' },
            { label: 'IMAGE4', value: 'image4' },
          ]}
          defaultValue={this.state.fileimage}
          containerStyle={{
            height: 40,
            borderRadius: 20,
            marginBottom: 10,
          }}
          style={{ backgroundColor: 'transparent' }}
          itemstyle={{ justifyContent: 'flex-start' }}
          labelStyle={{ color: 'white' }}
          dropDownStyle={{ backgroundColor: '#2F345D' }}
          onChangeItem={(item) => {
            this.setState({
              fileimage: item.value,
            });
          }}></DropdownPicker>
        <TextInput
          style={styles.inputbox}
          placeholder={'Title'}
          placeholderTextColor={'white'}
          onChangeText={(text) => {
            this.setState({
              title: text,
            });
          }}></TextInput>
        <TextInput
          style={styles.inputbox}
          placeholder={'Description'}
          placeholderTextColor={'white'}
          onChangeText={(text) => {
            this.setState({
              description: text,
            });
          }}></TextInput>
          <TextInput
          style={styles.inputbox}
          placeholder={'Story'}
          placeholderTextColor={'white'}
          onChangeText={(text) => {
            this.setState({
              story: text,
            });
          }}></TextInput>
        <TextInput
          style={styles.inputbox}
          placeholder={'Moral'}
          placeholderTextColor={'white'}
          onChangeText={(text) => {
            this.setState({
              moral: text,
            });
          }}></TextInput>
        <TouchableOpacity
          style={styles.button}
          onPress={() => {
            this.addstory();
          }}>
          <Text style={styles.buttontext}>Submit</Text>
        </TouchableOpacity>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#15193c',
  },
  header: {
    fontSize: 30,
    fontWeight: 'bold',
    color: 'white',
    alignSelf: 'center',
    marginTop: 30,
  },
  inputbox: {
    borderWidth: 2,
    margin: 10,
    borderColor: 'white',
    borderRadius: 5,
    fontSize: 24,
    color:'white'
  },
  displayimage: {
    width: '95%',
    height: 250,
    alignSelf: 'center',
    borderRadius: 30,
    resizeMode: 'contain',
  },
  button: {
    backgroundColor: 'white',
    width: 150,
    height: 50,
    borderRadius: 25,
    alignSelf: 'center',
    alignItems: 'center',
    justifyContent: 'center',
  },
  buttontext: {
    fontSize: 25,
    fontWeight: 'bold',
  },
});
