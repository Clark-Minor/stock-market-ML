import React, { Component } from 'react';
import { View, Image } from 'react-native';

export default class PresentData extends Component {
  render() {
    return (
      <View>
        <Image
          style={{width: 700, height: 400}}
          source={require('plots/aeo_last_2_years.png')}
        />
        <Image
          style={{width: 700, height: 400}}
          source={require('plots/aeo_last_2_years.png')}

        />
      }
    }
