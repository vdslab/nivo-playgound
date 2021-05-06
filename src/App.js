// import logo from "./logo.svg";
import "./App.css";
import data from "./data.json";
import { ResponsiveNetwork } from "@nivo/network";

function App() {
  return (
    <div className="App">
      {console.log(data)}
      <ResponsiveNetwork
        data={data}
        margin={{ top: 100, right: 100, bottom: 100, left: 100 }}
        repulsivity={100}
        iterations={60}
        nodeColor={function (e) {
          return e.color;
        }}
        nodeBorderWidth={1}
        nodeBorderColor={{ from: "color", modifiers: [["darker", 0.8]] }}
        linkThickness={function (e) {
          return 2 * (2 - e.source.depth);
        }}
        motionStiffness={160}
        motionDamping={12}
      />
      <p>HJNJN</p>
    </div>
  );
}
export default App;
