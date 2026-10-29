import { Canvas } from '@react-three/fiber';

export default function ThreeViewer() {
  return (
    <div className="viewer-panel">
      <Canvas>
        <ambientLight intensity={1.5} />
        <directionalLight position={[2, 2, 2]} />
        <mesh>
          <boxGeometry args={[1, 1, 1]} />
          <meshStandardMaterial color="#5eead4" />
        </mesh>
      </Canvas>
    </div>
  );
}
