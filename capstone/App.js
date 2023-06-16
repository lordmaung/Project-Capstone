import axios from 'axios';

axios.defaults.baseURL = 'http://34.101.173.241/api'; // Ganti URL server sesuai dengan server yang Anda miliki
axios.defaults.headers.common['Content-Type'] = 'application/json';

import React from 'react';
import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import Scheduler from './Scheduler';

const AppNavigator = createStackNavigator(
  {
    Scheduler: {
      screen: Scheduler,
      navigationOptions: {
        title: 'Scheduler',
      },
    },
  },
  {
    initialRouteName: 'Scheduler',
  }
);

export default createAppContainer(AppNavigator);
