import React, { Component } from "react";

class Form extends Component {
    handleSubmit(e) {
       e.preventDefault();
       this.props.onSubmit(this.state);
    }

    render() {
       return <React.Fragment>
           <h3>Add an appointment</h3>
           <form>
             <label>
               Date
               <input name="date" type="date" onChange={this.handleSubmit} />
             </label>
             <label>
               Room
               <input name="room_name" type="text" onChange={this.handleSubmit} />
             </label>
             <label>
               Start Time
               <input name="start_time" type="time" onChange={this.handleSubmit} />
             </label>
             <label>
               End Time
               <input name="end_time" type="time" onChange={this.handleSubmit} />
             </label>
             <button type="submit" id="form_submit" className="btn-default btn">
               Submit
             </button>
           </form>
         </React.Fragment>;
   }
}

export default Form;