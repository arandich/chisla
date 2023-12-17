<template>
  <div>
    <ImageUploader @startRecognition="handleImageRecognition" />
    <ResultViewer :result="recognitionResult" />
  </div>
</template>

<script>
import ImageUploader from './ImageUploader.vue'; // Путь к вашему компоненту ImageUploader
import ResultViewer from './ResultViewer.vue'; // Путь к вашему компоненту ResultViewer
import axios from 'axios';

export default {
  components: {
    ImageUploader,
    ResultViewer
  },
  data() {
    return {
      recognitionResult: null
    };
  },
  methods: {
    async handleImageRecognition(image) {
      try {
        const formData = new FormData();
        formData.append('image', image);

        const response = await axios.post('http://localhost:5000/api/recognize', formData);

        this.recognitionResult = response.data.result;
      } catch (error) {
        console.error('Ошибка при отправке изображения:', error);
      }
    }
  }
}
</script>

<style scoped>
/* Ваши стили для компонента */
</style>
