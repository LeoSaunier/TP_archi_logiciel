<script setup>
import QuestionnaireItem from './components/QuestionnaireItem.vue';
</script>

<template>
    <link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
  integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65"
  crossorigin="anonymous"/>
  <div>
    <h1>Gestion de questionnaires</h1>
  </div>
  <div>
    <h2>Questionnaires</h2>
    <ol>
      <QuestionnaireItem
        v-for="questionnaire in questionnaires">
      </QuestionnaireItem>
    </ol>
  </div>
  <div class="input-group">
 
  </div>
</template>

