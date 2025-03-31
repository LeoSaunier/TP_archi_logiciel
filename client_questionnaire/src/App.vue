<script>
import AllQuestionnaire from './components/AllQuestionnaire.vue';
import AjoutQuestionnaire from './components/AjoutQuestionnaire.vue';
import { update } from 'three/examples/jsm/libs/tween.module.js';
import { add } from 'three/tsl';


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
    UpdateQuestionnaire() {
      fetch("http://127.0.0.1:5000/quizz/api/v1.0/questionnaires")
    .then(response => response.json())
    .then(data => {
      this.questionnaires = data.questionnaires;
    });
    }

  },
  components: {
    AllQuestionnaire,
    AjoutQuestionnaire
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
    <AjoutQuestionnaire
    @UpdateQuestionnaire="UpdateQuestionnaire"
    ></AjoutQuestionnaire>
  </div>
  <div class="input-group">
 
  </div>
</template>
