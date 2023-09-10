import React, { useRef, useState, useEffect } from "react";
import { Canvas, useThree, useLoader } from "@react-three/fiber";
import {
  OrbitControls,
  PerspectiveCamera,
  Sky,
  Cloud,
  Environment,
} from "@react-three/drei";
import { BiSolidLeftArrow, BiSolidRightArrow } from "react-icons/bi";
import { PiCubeFocus } from "react-icons/pi";
import { gsap } from "gsap";
import { useSetRecoilState } from "recoil";
import { backgroundflagState } from "../../../recoil/atoms";
import { PLANET_LIST } from "../../../constants/constants";
import Button1 from "../../../common/atoms/Button1";
import * as THREE from "three";
import night from "./bg-night.jpg";
// import { EffectComposer, Bloom } from "@react-three/postprocessing";

// Cloud
function CloudsRenderer() {
  const cloudElements = [];

  for (let x = -400; x <= 400; x += 5) {
    cloudElements.push(
      <Cloud key={x} position={[x, -20, 0]} depth={3} segments={100} />,
    );
  }

  return <>{cloudElements}</>;
}

// 해당 컴포넌트를 사용하는 부모 컴포넌트 안에서
// <CloudsRenderer />를 사용하여 렌더링하면 됩니다.

// R3F 훅 카메라 컨트롤러 컴포넌트
function CameraController({ planet, zoomed }) {
  const { camera } = useThree();
  const cameraRef = useRef(camera);
  cameraRef.current = camera;
  const zoomFactor = 0.1;
  const multiFactor = 1.5;
  useEffect(() => {
    const targetPosition = zoomed
      ? {
          x: planet.x * multiFactor + 50,
          y: planet.y * multiFactor - 50,
          z: planet.z * multiFactor + 50,
        }
      : {
          x: planet.x * zoomFactor,
          y: planet.y * zoomFactor,
          z: planet.z * zoomFactor,
        };
    const startPosition = {
      x: camera.position.x,
      y: camera.position.y,
      z: camera.position.z,
    };

    const updateCameraPosition = () => {
      cameraRef.current.position.set(
        startPosition.x,
        startPosition.y,
        startPosition.z,
      );
      cameraRef.current.lookAt(0, 0, 0);
      cameraRef.current.updateProjectionMatrix();
    };

    gsap.to(startPosition, {
      duration: 2, // duration in seconds
      x: -targetPosition.x,
      y: -targetPosition.y,
      z: -targetPosition.z,
      onUpdate: updateCameraPosition,
      ease: "power1.inOut", // easing function for smooth transition
    });
  }, [planet, zoomed]);

  return null;
}

const ListSectionPlanet = ({ currentPlanet, setCurrentPlanet }) => {
  // 배경화면 flag
  const setBackgroundflag = useSetRecoilState(backgroundflagState);
  useEffect(() => {
    setBackgroundflag(false);
  }, []);
  const [zoomed, setZoomed] = useState(false);

  useEffect(() => {
    // useEffect로 현재 행성이 바뀔 때마다 Update하기
  }, [currentPlanet]);

  const [buttonClicked, setButtonClicked] = useState(false);

  const handleButtonClick = (direction) => {
    if (buttonClicked) return;

    setButtonClicked(true); // 버튼이 눌렸음을 상태에 저장

    setTimeout(() => {
      setButtonClicked(false);
    }, 1000);

    if (direction === "left") {
      setCurrentPlanet((prevIndex) =>
        prevIndex === 0 ? PLANET_LIST.length - 1 : prevIndex - 1,
      );
    } else if (direction === "right") {
      setCurrentPlanet((prevIndex) =>
        prevIndex === PLANET_LIST.length - 1 ? 0 : prevIndex + 1,
      );
    }
  };

  const preventKeyClick = (e) => {
    if (e.key === "Enter" || e.key === " ") e.preventDefault();
  };
  // 확대축소 버튼
  const handleZoomClick = () => {
    setZoomed(!zoomed);
  };

  return (
    <div className="absolute flex h-full w-full flex-row flex-wrap justify-center">
      <button
        className="absolute left-4 top-1/2 z-10 flex flex-col text-4xl text-white opacity-50"
        onClick={() => handleButtonClick("left")}
        onKeyDown={preventKeyClick}
      >
        <BiSolidLeftArrow />
      </button>
      <button
        className="absolute right-4 top-1/2 z-10 flex flex-col text-4xl text-white opacity-50"
        onClick={() => handleButtonClick("right")}
        onKeyDown={preventKeyClick}
      >
        <BiSolidRightArrow />
      </button>
      <Button1
        className="absolute bottom-24 right-4 z-10 mx-auto my-auto flex inline-flex flex-col items-center justify-center rounded-full border p-2 text-4xl text-white opacity-100"
        onClick={handleZoomClick}
        icon={<PiCubeFocus size={30} />}
      />
      <button className="absolute top-0 z-10 rounded-full bg-blue-500 p-2 text-white">
        Goto Ocean
      </button>
      <Canvas camera={{ position: [0, 50, 0] }}>
        <axesHelper args={[100]} />
        <OrbitControls
          enabled={true}
          rotateSpeed={-0.5}
          enablePan={false}
          minDistance={0}
          maxDistance={100}
          autoRotate={true}
          autoRotateSpeed={0.5}
        />
        <PerspectiveCamera makeDefault near={0.1} far={200} fov={60} />
        <CameraController planet={PLANET_LIST[currentPlanet]} zoomed={zoomed} />
        {/* <EffectComposer>
          <Bloom luminanceThreshold={0} luminanceSmoothing={0.9} height={100} />
        </EffectComposer> */}
        <CloudsRenderer />
        <Sky
          distance={3000}
          sunPosition={[1, 1, 0]}
          inclination={0.5}
          azimuth={0.1}
          mieCoefficient={0.003}
          rayleigh={0.1}
        />
        <ambientLight intensity={3} />
        <>
          <Environment background blur={0} preset="park" />
          <mesh position={[50, 5, 0]}>
            <sphereGeometry args={[5, 32, 32]} />
            <meshStandardMaterial metalness={1} roughness={0} />
          </mesh>
        </>
        <mesh position={[50, 5, 50]}>
          <sphereGeometry args={[5, 32, 32]} />
          <meshNormalMaterial
          // envMap={texture}
          // metalness={1}
          // roughness={0}
          // color="blue"
          />
        </mesh>
        <mesh position={[0, 5, 50]}>
          <sphereGeometry args={[5, 32, 32]} />
          <meshStandardMaterial
            // color="blue"
            map={useLoader(THREE.TextureLoader, night)}
            // metalness={0.8}
            roughness={0.5}
            flatShading={false}
          />
        </mesh>
      </Canvas>
    </div>
  );
};

export default ListSectionPlanet;
