<template>
  <div>
    <input type="file" @change="handleFileChange">
    <button @click="startRecognition" :disabled="!image">Начать распознавание</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      image: null
    };
  },
  methods: {
    handleFileChange(event) {
      this.image = event.target.files[0];
    },
    startRecognition() {
      if (this.image) {
        this.$emit('startRecognition', this.image);
      }
    }
  }
}
</script>

<style scoped>
/* Ваши стили для компонента */
</style>
