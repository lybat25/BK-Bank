<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Подсчёт прыжков на скакалке</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
            padding: 20px;
        }

        #video {
            width: 80%;
            max-width: 600px;
            border: 1px solid #ccc;
            margin-bottom: 20px;
        }

        #status {
            font-size: 18px;
            color: #333;
        }

        .video-container {
            position: relative;
            display: inline-block;
        }

        #canvas {
            position: absolute;
            top: 0;
            left: 0;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <h1>Подсчёт прыжков на скакалке</h1>
    
    <div class="video-container">
        <video id="video" autoplay></video>
        <canvas id="canvas"></canvas>
    </div>

    <div id="status">Загрузка модели...</div>
    <div id="jump-count">Прыжков: 0</div>

    <!-- Подключаем TensorFlow.js и PoseNet -->
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/posenet"></script>

    <script>
        const video = document.getElementById('video');
        const canvas = document.getElementById('canvas');
        const context = canvas.getContext('2d');
        const status = document.getElementById('status');
        const jumpCountElement = document.getElementById('jump-count');

        let jumpCount = 0;
        let isJumping = false;
        let baselineY = null; // Базовая линия для калибровки

        async function setupCamera() {
            if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
                status.innerText = 'Ваш браузер не поддерживает доступ к камере';
                return;
            }

            try {
                const stream = await navigator.mediaDevices.getUserMedia({
                    video: { width: 640, height: 480 }
                });
                video.srcObject = stream;

                return new Promise((resolve) => {
                    video.onloadedmetadata = () => {
                        resolve();
                    };
                });
            } catch (error) {
                status.innerText = 'Ошибка доступа к камере';
                console.error(error);
            }
        }

        async function loadModel() {
            status.innerText = 'Загрузка модели PoseNet...';
            const model = await posenet.load({
                architecture: 'MobileNetV1',
                outputStride: 16,
                inputResolution: { width: 640, height: 480 },
                multiplier: 0.75
            });
            status.innerText = 'Модель загружена! Начинаю анализировать...';
            analyzeFrame(model);
        }

        async function analyzeFrame(model) {
            const pose = await model.estimateSinglePose(video, {
                flipHorizontal: false
            });

            drawPose(pose);
            detectJump(pose);

            requestAnimationFrame(() => analyzeFrame(model));
        }

        function drawPose(pose) {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;

            context.clearRect(0, 0, canvas.width, canvas.height);

            // Рисуем ключевые точки
            pose.keypoints.forEach(keypoint => {
                if (keypoint.score > 0.5) {
                    context.beginPath();
                    context.arc(keypoint.position.x, keypoint.position.y, 5, 0, 2 * Math.PI);
                    context.fillStyle = 'red';
                    context.fill();
                }
            });
        }

        function detectJump(pose) {
            const leftAnkle = pose.keypoints.find(k => k.part === 'leftAnkle');
            const rightAnkle = pose.keypoints.find(k => k.part === 'rightAnkle');

            if (leftAnkle && rightAnkle && leftAnkle.score > 0.5 && rightAnkle.score > 0.5) {
                const avgY = (leftAnkle.position.y + rightAnkle.position.y) / 2;

                // Калибровка: устанавливаем базовую линию при первом кадре
                if (baselineY === null) {
                    baselineY = avgY;
                    status.innerText = 'Калибровка завершена. Начинайте прыжки!';
                }

                // Определяем прыжок
                const jumpThreshold = 50; // Порог для прыжка (в пикселях)
                if (avgY < baselineY - jumpThreshold && !isJumping) {
                    isJumping = true;
                    jumpCount++;
                    jumpCountElement.innerText = Прыжков: ${jumpCount};
                } else if (avgY >= baselineY - jumpThreshold) {
                    isJumping = false;
                }
            }
        }

        async function init() {
            await setupCamera();
            await loadModel();
        }

        init();
    </script>
</body>
</html>
