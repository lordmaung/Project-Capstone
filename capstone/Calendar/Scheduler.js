import React, { useEffect, useState } from 'react';
import { View, StyleSheet, Alert } from 'react-native';
import { ScheduleComponent, ViewsDirective, ViewDirective, Day, Week, Month, DragAndDrop, Inject } from '@syncfusion/ej2-react-schedule';
import axios from 'axios';

const Scheduler = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('/tasks');
      setTasks(response.data);
    } catch (error) {
      console.error(error);
      Alert.alert('Error', 'Failed to fetch data from the server.');
    }
  };

  return (
    <View style={styles.container}>
      <ScheduleComponent
        currentView='Month'
        eventSettings={{ dataSource: tasks }}
      >
        <ViewsDirective>
          <ViewDirective option='Day' />
          <ViewDirective option='Week' />
          <ViewDirective option='Month' />
        </ViewsDirective>
        <Inject services={[Day, Week, Month, DragAndDrop]} />
      </ScheduleComponent>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});

export default Scheduler;
