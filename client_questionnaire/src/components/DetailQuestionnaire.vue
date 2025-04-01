<script>
import { ref, watch } from 'vue';
import AllQuestion from './AllQuestion.vue';

export default {
    props: {
        questionnaire: Object,
        questions: Array,
        name: String,
    },
    setup(props) {
        const selectedQuestionType = ref(null);
        const Q1selected = ref(false);
        const Q2selected = ref(false);
        const question = ref({ title: '', description: '', propositions: ['', ''] });
        const name = ref(props.questionnaire?.name || ''); // Initialiser avec le nom du questionnaire

        watch(selectedQuestionType, (newValue) => {
            Q1selected.value = newValue === 'Q1';
            Q2selected.value = newValue === 'Q2';
        });

        return { selectedQuestionType, Q1selected, Q2selected, question, name };
    },
    components: {
        AllQuestion
    },
    methods: {
        modifyQuestionnaire() {
            console.log("modifyQuestionnaire", this.name);
            this.$emit('modifyQuestionnaire', this.questionnaire, this.name);
        },
        addQuestionOuverte() {
            this.$emit('addQuestionOuverte', { ...this.question, type: 'Q1' });
        },
        addQuestionSimple() {
            this.$emit('addQuestionSimple', { ...this.question, type: 'Q2' });
        },
        selectQuestion() {
            console.log("selectQuestion");
        },
        deleteQuestion() {
            console.log('Deleting question:', this.questionnaire);
            this.$emit('deleteQuestion', this.questionnaire);
        }
    },
    emits: ['modifyQuestionnaire', 'addQuestionOuverte', 'addQuestionSimple', 'deleteQuestion'],
};
</script>

<template>
    <div>
        <div>
            <input type="text" v-model="this.name" placeholder="Questionnaire Name">
            <button @click="modifyQuestionnaire">Modify</button>
        </div> 
        <AllQuestion
            :questions="questions"
            @questionDeleted="deleteQuestion"
        >
        </AllQuestion>
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
                    <input type="text" v-model="question.awnser" placeholder="Réponse">
                </label>
                <button class="btn btn-add" @click="addQuestionOuverte">Ajouter</button>
            </div>
            
            <div v-if="Q2selected">
                <label>
                    <input type="text" v-model="question.title" placeholder="Nom de la question">
                    <input type="text" v-model="question.awnser" placeholder="Réponse">
                    <input type="text" v-model="question.propositions[0]" placeholder="Proposition 1">
                    <input type="text" v-model="question.propositions[1]" placeholder="Proposition 2">
                </label>
                <button class="btn btn-add" @click="addQuestionSimple">Ajouter</button>
            </div>
        </div>
    </div>
</template>
