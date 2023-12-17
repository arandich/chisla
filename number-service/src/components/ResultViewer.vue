<template>
  <div>
    <h2>Результат распознавания:</h2>
    <div v-if="result">{{ result }}</div>
    <div v-else>Ожидание результата...</div>
  </div>
</template>

<script>
export default {
  props: {
    result: String
  }
}
</script>

<style scoped>
/* Ваши стили для компонента */
</style>
