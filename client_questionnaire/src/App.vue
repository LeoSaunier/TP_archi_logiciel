<script>
import AllQuestionnaire from './components/AllQuestionnaire.vue';
import AjoutQuestionnaire from './components/AjoutQuestionnaire.vue';
import DetailQuestionnaire from './components/DetailQuestionnaire.vue';
import { ref } from 'vue';


export default {
  data() {
    return {
      questionnaires: [],
      questionnaire: ref(null),
      questions: Array,
    };
  },
  methods: {
    deleteQuestionnaire(questionnaire) {
      this.questionnaires = this.questionnaires.filter(q => q !== questionnaire);
    },
    UpdateQuestionnaire() {
      this.questionnaires = null;
      this.questions = null;
      fetch("http://127.0.0.1:5000/quizz/api/v1.0/questionnaires")
    .then(response => response.json())
    .then(data => {
      this.questionnaires = data.questionnaires;
    });
    },
    selectQuestionnaire(questionnaire) {
      this.questionnaire = {...questionnaire};
      fetch(questionnaire.uri+"/questions")
      .then(response => response.json())
      .then(data => {
        this.questions = data.questions;
      });
    },
    modifyQuestionnaire(questionnaire, name) {
      this.questionnaire = questionnaire;
      fetch(questionnaire.uri,{
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name: name }),
                method: "PUT",
            })
            .then(response => {
                if (response.ok) {
                    console.log("Questionnaire modified successfully");
                    this.UpdateQuestionnaire();
                } else if (response.status === 404) {
                    console.error("Questionnaire not found");
                } else if (response.status === 403) {
                    console.error("You do not have permission to modify this questionnaire");
                } else if (response.status === 500) {
                    console.error("Server error while modifying questionnaire");
                } else {
                    console.error("Failed to modify questionnaire");
                }
            })
    },

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
    :questions="questions"
    :name="questionnaire.name"
    @deleteQuestion="selectQuestionnaire"
    @modifyQuestionnaire="modifyQuestionnaire"
    @updateQuestionnaire="selectQuestionnaire"
    ></DetailQuestionnaire>
  </div>
  <div class="input-group">
 
  </div>
</template>
