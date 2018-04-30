import React, { Component } from "react";
import Form from "./Form";

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
    return <React.Fragment>
        <div className="list">
          {this.state.appointments.map(item => <div key={item.id}>
              <h2>
                > {item.start_time} to {item.end_time} at {item.room_name}
              </h2>
              <span className="dates">{item.date}</span>
            </div>)}
        </div>
        <p />
        <Form />
      </React.Fragment>;
  }
}

export default App;
