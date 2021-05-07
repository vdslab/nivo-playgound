// import logo from "./logo.svg";
import "./App.css";
import networkData from "./networkData.json";
import bumpData from "./bumpData.json";
import ResponsiveNetwork from "./responsiveNetwork.js";
import ResponsiveBump from "./responsiveBump.js";

function App() {
  return (
    <div className="App">
      
      <ResponsiveNetwork data={networkData} />
      <ResponsiveBump data={bumpData} />
    </div>
  );
}
export default App;
