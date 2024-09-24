import argparse
from utils.data_utils import parse_list
from utils.gen_utils import generate_ans

if __name__ == "__main__":
    """
    Generate answers from a specified model and save the results to files.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--model_name", type=str, default="gpt-4o")

    parser.add_argument("--api_key", type=str,
                        default='sk-xxx')

    parser.add_argument("--data_dir", type=str,
                        default="./data", help="The parent dir of dataset")

    parser.add_argument("--subset_name", type=str, default=None,
                        help="name for the dataset, English / Chinese / French. If None, we will generate all the sub datasets.")

    parser.add_argument("--question_ids", type=parse_list, default=None,
                        help="list of question ids to query. If None, we will run over all the questions in the subset")

    parser.add_argument("--save_dir", type=str, default="./result",
                        help="The local dir to save the generation result")
    
    parser.add_argument("--mc_answer_extraction_method", type=str, default="regex",
                        help="The method of extracting option values from LLM's response. (regex / gpt-4o)")
    
    parser.add_argument("--gpt4o_apikey", type=str, default=None,
                        help="If mc_answer_extraction_method is gpt-4o, then you need to fill in")

    args = parser.parse_args()

    generate_ans(args.model_name, args.api_key, args.data_dir,
                 args.subset_name, args.save_dir, args.question_ids, 
                 args.mc_answer_extraction_method, args.gpt4o_apikey)
