<script>
import { ref, watch } from 'vue';
import AllQuestion from './AllQuestion.vue';
import DetailsQuestion from './DetailsQuestion.vue';

export default {
    props: {
        questionnaire: Object,
        questions: Array,
        question: Object,
    },
    setup(props) {
        const selectedQuestionType = ref(null);
        const Q1selected = ref(false);
        const Q2selected = ref(false);
        const question = ref({ title: '', description: '', propositions: ['', ''] });

        watch(selectedQuestionType, (newValue) => {
            Q1selected.value = newValue === 'Q1';
            Q2selected.value = newValue === 'Q2';
        });

        return { selectedQuestionType, Q1selected, Q2selected, question };
    },
    components: {
        AllQuestion,
        DetailsQuestion,
    },
    methods: {
        modifyQuestionnaire() {
            console.log("modifyQuestionnaire", this.questionnaire.name);
            this.$emit('modifyQuestionnaire', this.questionnaire, this.questionnaire.name);
        },
        addQuestionOuverte() {
            this.$emit('addQuestionOuverte', { ...this.question, type: 'Q1' });
        },
        addQuestionSimple() {
            this.$emit('addQuestionSimple', { ...this.question, type: 'Q2' });
        },
        selectQuestion(question) {
            this.question = {...question};
            console.log("selectQuestion");
        },
        deleteQuestion() {
            console.log('Deleting question:', this.questionnaire);
            this.$emit('deleteQuestion', this.questionnaire);
        },
        modifyQuestion(question) {
            console.log("modifyQuestion", question);
            const request = {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(question),
            };
            fetch(question.uri, request)
                .then(response => {
                    if (response.ok) {
                        console.log("Question modified successfully");
                        this.$emit('updateQuestionnaire', this.questionnaire);
                        this.reponse = null;
                    } else if (response.status === 404) {
                        console.error("Question not found");
                    } else if (response.status === 403) {
                        console.error("You do not have permission to modify this question");
                    } else if (response.status === 500) {
                        console.error("Server error while modifying question");
                    } else {
                        console.error("Failed to modify question");
                    }
                })
                .catch(error => {
                    console.error("Error modifying question:", error);
                });
        },
    },
    emits: ['modifyQuestionnaire', 'addQuestionOuverte', 'addQuestionSimple', 'deleteQuestion'],
};
</script>

<template>
    <div>
        <div>
            <input type="text" v-model="this.questionnaire.name" placeholder="Questionnaire Name">
            <button @click="modifyQuestionnaire">Modify</button>
        </div> 
        <AllQuestion
            :questions="questions"
            @questionDeleted="deleteQuestion"
            @selectQuestion="selectQuestion"
        >
        </AllQuestion>
        <DetailsQuestion 
            v-if="question && question.title" 
            :question="question"
            @updateQuestion="modifyQuestion"
        >
        </DetailsQuestion>

        <div>
            <fieldset>
                <legend>Type de question :</legend>
                <div>
                    <input type="radio" id="Q1" value="Q1" v-model="selectedQuestionType" />
                    <label for="Q1">Question ouverte</label>
                </div>
                <div>
                    <input type="radio" id="Q2" value="Q2" v-model="selectedQuestionType" />
                    <label for="Q2">Question simple</label>
                </div>
            </fieldset>

            <div v-if="Q1selected">
                <label>
                    <input type="text" v-model="question.title" placeholder="Nom de la question">
                    <input type="text" v-model="question.reponse" placeholder="Réponse">
                </label>
                <button class="btn btn-add" @click="addQuestionOuverte">Ajouter</button>
            </div>
            
            <div v-if="Q2selected">
                <label>
                    <input type="text" v-model="question.title" placeholder="Nom de la question">
                    <input type="number" v-model="question.reponse" placeholder="Réponse">
                    <input type="text" v-model="question.propositions[0]" placeholder="Proposition 1">
                    <input type="text" v-model="question.propositions[1]" placeholder="Proposition 2">
                </label>
                <button class="btn btn-add" @click="addQuestionSimple">Ajouter</button>
            </div>
        </div>
    </div>
</template>
