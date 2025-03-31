<script>
import QuestionnaireItem from './components/QuestionnaireItem.vue';

let selectQuestionnaire = (questionnaire) => {
  console.log('Selected questionnaire:', questionnaire);
  // Here you can add logic to handle the selected questionnaire
  // For example, you might want to navigate to a different page or show more details
  // this.$router.push({ name: 'questionnaireDetails', params: { id: questionnaire.id } });
};


export default {
  data() {
    return {
      questionnaires: []
    };
  },
  components: {
    QuestionnaireItem
  },
  methods: {
    selectQuestionnaire,
    deleteQuestionnaire: function (questionnaire) {
      console.log('Deleted questionnaire:', questionnaire);
  fetch(questionnaire.uri,{
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: "DELETE"
            }).then(response => {
                if (response.ok) {
                    console.log("Questionnaire deleted successfully");
                    this.questionnaires = this.questionnaires.filter(q => q.uri !== questionnaire.uri);
                } else if (response.status === 404) {
                    console.error("Questionnaire not found");
                } else if (response.status === 403) {
                    console.error("You do not have permission to delete this questionnaire");
                } else if (response.status === 500) {
                    console.error("Server error while deleting questionnaire");
                } else {
                    console.error("Failed to delete questionnaire");
                }
            })
            .catch(error => {
                console.error("Error deleting questionnaire:", error);
            });
    }
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
    <ol>
      <QuestionnaireItem
        v-for="questionnaire in questionnaires"
        :questionnaire="questionnaire"
        @selectQuestionnaire="selectQuestionnaire"
        @deleteQuestionnaire="deleteQuestionnaire">
      </QuestionnaireItem>
    </ol>
  </div>
  <div class="input-group">
 
  </div>
</template>
