import networkData from "./networkData.json";
import bumpData from "./genres_data.json";
import ResponsiveNetwork from "./components/responsiveNetwork.js";
import ResponsiveBump from "./components/responsiveBump.js";

function App() {
  return (
    <div className="App">
      <ResponsiveNetwork data={networkData} />
      <ResponsiveBump data={bumpData} />
    </div>
  );
}
export default App;
