<script>
import QuestionnaireItem from './components/QuestionnaireItem.vue';
import AllQuestionnaire from './components/AllQuestionnaire.vue';
import { update } from 'three/examples/jsm/libs/tween.module.js';


export default {
  data() {
    return {
      questionnaires: []
    };
  },
  methods: {
    deleteQuestionnaire(questionnaire) {
      this.questionnaires = this.questionnaires.filter(q => q !== questionnaire);
    },
  },
  components: {
    AllQuestionnaire
  },
  mounted() {
    fetch("http://127.0.0.1:5000/quizz/api/v1.0/questionnaires")
    .then(response => response.json())
    .then(data => {
      this.questionnaires = data.questionnaires;
    });
  }
};

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
    <AllQuestionnaire
    :questionnaires="questionnaires"
    @questionnaireDeleted="deleteQuestionnaire"
    >
    </AllQuestionnaire>
  </div>
  <div class="input-group">
 
  </div>
</template>
=======
<script setup>
import QuestionnaireItem from './components/QuestionnaireItem.vue';
import AjoutQuestionnaire from './components/AjoutQuestionnaire.vue';
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
      v-for="questionnaire in questionnaires"
      :questionnaire="questionnaire"
      @selectQuestionnaire="selectQuestionnaire"
      @deleteQuestionnaire="deleteQuestionnaire">
    </QuestionnaireItem>
  </ol>
</div>
<AjoutQuestionnaire></AjoutQuestionnaire>
</template>

