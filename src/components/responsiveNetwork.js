import { ResponsiveNetwork } from "@nivo/network";

const MyResponsiveNetwork = ({ data /* see data tab */ }) => {
  console.log(data);
  return (
    <div style={{ width: "1600px", height: "600px" }}>
      <ResponsiveNetwork
        // data={data}
        nodes={data.nodes}
        links={data.links}
        margin={{ top: 100, right: 200, bottom: 0, left: 0 }}
        repulsivity={1000}
        iterations={60}
        nodeColor={function (e) {
          return e.color;
        }}
        nodeBorderWidth={2}
        nodeBorderColor={{ from: "color", modifiers: [["darker", 0.8]] }}
        linkThickness={function (e) {
          return 2 * (2 - e.source.depth);
        }}
        motionStiffness={16}
        motionDamping={5}
      />
    </div>
    // <ResponsiveNetwork
    //   data={data}
    //   margin={{ top: 0, right: 0, bottom: 0, left: 0 }}
    //   repulsivity={6}
    //   iterations={60}
    //   nodeColor={function (e) {
    //     return e.color;
    //   }}
    //   nodeBorderWidth={1}
    //   nodeBorderColor={{ from: "color", modifiers: [["darker", 0.8]] }}
    //   linkThickness={function (e) {
    //     return 2 * (2 - e.source.depth);
    //   }}
    //   motionStiffness={160}
    //   motionDamping={12}
    // />
  );
};
export default MyResponsiveNetwork;
