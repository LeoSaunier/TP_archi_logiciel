<script>
import AllQuestionnaire from './components/AllQuestionnaire.vue';
import AjoutQuestionnaire from './components/AjoutQuestionnaire.vue';
import DetailQuestionnaire from './components/DetailQuestionnaire.vue';
import { ref } from 'vue';


export default {
  data() {
    return {
      questionnaires: [],
      questionnaire: ref(null)
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
    },
    selectQuestionnaire(questionnaire) {
      this.questionnaire = questionnaire.uri;
    }

  },
  components: {
    AllQuestionnaire,
    AjoutQuestionnaire,
    DetailQuestionnaire
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
    @selectQuestionnaire="selectQuestionnaire"
    >
    </AllQuestionnaire>
    <AjoutQuestionnaire
    @UpdateQuestionnaire="UpdateQuestionnaire"
    ></AjoutQuestionnaire>
    <DetailQuestionnaire 
    v-if="questionnaire != null"
    :questionnaire="questionnaire"
    ></DetailQuestionnaire>
  </div>
  <div class="input-group">
 
  </div>
</template>
