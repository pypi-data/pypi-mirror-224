from shapes_recognition.src.save_results import save_self_study_results, save_recognition_results
from shapes_recognition.src.draw_results import draw_self_study_results, draw_recognition_results


def show_self_study_results(list_self_study_in,
                            list_self_study_out):

    save_self_study_results(list_self_study_in,
                            list_self_study_out)

    draw_self_study_results(list_self_study_in,
                            list_self_study_out)


def show_recognition_results(recogn_dictionary):

    save_recognition_results(recogn_dictionary)

    draw_recognition_results(recogn_dictionary)
