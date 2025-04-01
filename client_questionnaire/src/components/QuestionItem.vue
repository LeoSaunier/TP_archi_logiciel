<script>

export default {
    props: {
        question: Object
    },
    methods: {
        deleteQuestion() {
            this.$emit('deleteQuestion', this.question);
        },
        selectQuestion() {
            console.log("selectQuestion");
        }
    },
    emits: ['deleteQuestion', 'selectQuestion'],
}

</script>


<template>
        <div class="question-item">
            <button class="question-item-btn" @click="selected = !selected">
                <h4>{{ question.title }}</h4>
                <p>{{ question.questionType }}</p>
            </button>
            <button class="btn btn-delete" @click="deleteQuestion">Supprimer</button>
        </div>
</template>