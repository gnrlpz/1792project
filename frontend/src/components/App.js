import React, { Component } from "react";

class App extends Component {
  state = {
    appointments: []
  };

  async componentDidMount() {
    try {
      const res = await fetch("http://127.0.0.1:8000/reservation/appointments/");
      const appointments = await res.json();
      this.setState({
        appointments
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div className="list">
        {this.state.appointments.map(item => (
          <div key={item.id}>
            <h2>{item.start_time} to {item.end_time} at {item.room_name}</h2>
            <span>{item.date}</span>
          </div>
        ))}
        
      </div>
    );
  }
}

export default App;
