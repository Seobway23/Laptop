import * as THREE from "three";
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

class App {
	constructor() {
		const divContainer = document.querySelector("#webgl-container");
		this._divContainer = divContainer;

		const renderer = new THREE.WebGLRenderer({ antialias: true });
		renderer.setPixelRatio(window.devicePixelRatio);
		divContainer.appendChild(renderer.domElement);
		this._renderer = renderer;

		const scene = new THREE.Scene();
		this._scene = scene;

		this._setupCamera();
		this._setupLight();
		this._setupModel();
		this._setControls();
        this._update_position();

		window.onresize = this.resize.bind(this);
		this.resize();

		requestAnimationFrame(this.render.bind(this));

        // raycaster 초기화
        this._raycaster = new THREE.Raycaster();
	}

	_setupCamera() {
		const width = this._divContainer.clientWidth;
		const height = this._divContainer.clientHeight;
		const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 100000);
		camera.position.z = 10;
        camera.lookAt(new THREE.Vector3(0, 0, 0)); // 원하는 방향으로 설정
		this._camera = camera;

	}

	_setupLight() {
		const color = 0xffffff;
		const intensity = 1;
		const light = new THREE.DirectionalLight(color, intensity);
		light.position.set(-1, 2, 4);
		this._scene.add(light);
	}

	// _setupModel() {
	// 	const geometry = new THREE.S(1, 1, 1);
	// 	const fillmaterial = new THREE.MeshPhongMaterial({ color: 0x44a88  });
	// 	const cube = new THREE.Mesh(geometry, fillmaterial);
	// 	// const cube = new THREE.Mesh(geometry, material);
		
	// 	const lineMaterial = new THREE.LineBasicMaterial({color: 0x44a88 });
	// 	const line = new THREE.LineSegments(
	// 		new THREE.WireframeGeometry(geometry), lineMaterial,
	// 	)

	// 	this._scene.add(cube);
	// 	this._cube = cube;
	// }

    // // setcontorl 초기
	// _setControls() {
	// 	new OrbitControls(this._camera, this._divContainer);
	// }


// 수정
    _setControls() {
        const controls = new OrbitControls(this._camera, this._divContainer);

        this._divContainer.addEventListener('change', this._handleControlsChange.bind(this));
        this._divContainer.addEventListener('click', this._handleSphereClick.bind(this));
        this._controls = controls;
        

    }
    _handleControlsChange() {
        // 필요한 경우 처리할 로직 추가
    }
    
    _handleSphereClick(event) {
        event.preventDefault();
        
        this._raycaster.setFromCamera({ x: 0, y: 0 }, this._camera);
        
        // console.log(this._raycaster)
        const intersects = this._raycaster.intersectObject(this._particle);
    
        if (intersects.length > 0) {
            // 클릭한 별에게 접근 가능, 
            console.log('intersects:' , intersects[0].object.position);
            const targetUrl = 'h1/index.html'
            window.location.href = targetUrl;
        }
    }
    
// 수정



	_setupModel() {
        let particle, material;
            const geometry = new THREE.SphereGeometry(5, 50, 50);
            // const color = new THREE.Color(Math.random() * 0xffffff);

            material = new THREE.ShaderMaterial({
                uniforms: {
                    globeTexture: {
                        value: new THREE.TextureLoader().load("data/123.jpg")
                    }
                },
                vertexShader: `
                    varying vec2 vertexUV;
                    varying vec3 vertexNormal;
                    void main() {
                        vertexUV = uv;
                        vertexNormal = normalize(normalMatrix * normal);
                        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
                    }
                `,
                fragmentShader: `
                    uniform sampler2D globeTexture;
                    varying vec2 vertexUV;
                    varying vec3 vertexNormal;
                    void main() {
                    float intensity = 1.05 - dot(vertexNormal, vec3(0.,0.,1.));
                    vec3 atmosphere = vec3(0.3, 0.6, 1.0) * pow(intensity, 1.5);
                    vec4 color = texture2D(globeTexture, vertexUV);
                    gl_FragColor = vec4(atmosphere + color.xyz, 1.);
                    }
                `,
            })
            
            const atmosphere = new THREE.Mesh(
                new THREE.SphereGeometry(5, 50, 50),
                new THREE.ShaderMaterial({
                    vertexShader: `
                        varying vec3 vertexNormal;
                        void main() {
                            vertexNormal = normalize(normalMatrix * normal);
                            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
                        }
                    `,
                    fragmentShader: `
                        varying vec3 vertexNormal;
                        void main() {
                            float intensity = pow(0.76 - dot(vertexNormal, vec3(0,0,1.)), 2.0);
                            gl_FragColor = vec4(0.3, 0.6, 1.0, 1) * intensity;
                        }
                    `,
                    transparent: true,
                    blending: THREE.AdditiveBlending,
                    side: THREE.BackSide
                })
            );
            atmosphere.scale.set(1.1, 1.1, 1.1);
            
            console.log('atmosphere:',atmosphere)
            this._scene.add(atmosphere)
            


            // material = new THREE.MeshBasicMaterial({color: 0xffffff});
            particle = new THREE.Mesh(geometry, material);

            particle.position.x = 1;
            particle.position.y = 1;
            particle.position.z = 1;

            this._scene.add(particle);
            this._particle = particle;
            console.log(particle);
    }
    

	resize() {
		const width = this._divContainer.clientWidth;
		const height = this._divContainer.clientHeight;

		this._camera.aspect = width / height;
		this._camera.updateProjectionMatrix();

		this._renderer.setSize(width, height);
	}

	render(time) {
		this._renderer.render(this._scene, this._camera);
		this.update(time);
		requestAnimationFrame(this.render.bind(this));
	}
    
	update(time) {
		time *= 0.0001; // secondunit
		// this._cube.rotation.x = time;
		this._particle.rotation.y = time;
		this._particle.rotation.z = time;
        // console.log(this._particle)

	}

    _update_position() {
        console.log('x: ',this._particle.position.x,'   ','y:',this._particle.position.y)
        
    }
}

window.onload = function () {
	new App();
};