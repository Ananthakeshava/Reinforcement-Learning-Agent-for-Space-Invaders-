# """
# Main entry point for Space Invaders DQN Project
# Provides a command-line interface for training and testing the agent
# """

# import sys
# import ale_py
# import gymnasium as gym

# # Force register the Atari environments into Gymnasium
# gym.register_envs(ale_py)

# # Inject Gymnasium into sys.modules so any file trying to run `import gym` 
# # gets redirected to the working, modern `gymnasium` instead!
# sys.modules['gym'] = gym

# import argparse
# import sys
# import os
# from datetime import datetime

# import numpy as np
# import tensorflow as tf

# from train import main as train_main
# from test_agent import main as test_main
# from utils import create_environment, print_environment_info


# def print_banner():
#     """Print project banner"""
#     banner = """
#     ╔══════════════════════════════════════════════════════════════╗
#     ║                                                              ║
#     ║              🚀 SPACE INVADERS DQN PROJECT 🚀                ║
#     ║                                                              ║
#     ║         Deep Reinforcement Learning with Keras & TF         ║
#     ║                                                              ║
#     ╚══════════════════════════════════════════════════════════════╝
#     """
#     print(banner)


# # def check_dependencies():
# #     """Check if all required dependencies are installed"""
# #     required_packages = [
# #         'tensorflow',
# #         'keras-rl2',
# #         'gym',
# #         'gymnasium',
# #         'opencv-python',
# #         'numpy',
# #         'matplotlib'
# #     ]
    
# #     missing_packages = []
    
# #     for package in required_packages:
# #         try:
# #             __import__(package.replace('-', '_'))
# #         except ImportError:
# #             missing_packages.append(package)
    
# #     if missing_packages:
# #         print("❌ Missing required packages:")
# #         for package in missing_packages:
# #             print(f"   - {package}")
# #         print("\nPlease install missing packages using:")
# #         print("pip install -r requirements.txt")
# #         return False
    
# #     print("✅ All required packages are installed!")
# #     return True


# def check_dependencies():
#     """Check if all required dependencies are installed"""

#     # Mapping: Display Name -> Python Import Name
#     required_packages = {
#         "tensorflow": "tensorflow",
#         "keras-rl2": "rl",
#         "gym": "gym",
#         "gymnasium": "gymnasium",
#         "opencv-python": "cv2",
#         "numpy": "numpy",
#         "matplotlib": "matplotlib",
#     }

#     missing_packages = []

#     for package_name, module_name in required_packages.items():
#         try:
#             __import__(module_name)
#         except ImportError:
#             missing_packages.append(package_name)

#     if missing_packages:
#         print("❌ Missing required packages:")
#         for package in missing_packages:
#             print(f"   - {package}")
#         print("\nPlease install missing packages using:")
#         print("pip install -r requirements.txt")
#         return False

#     print("✅ All required packages are installed!")
#     return True

# def test_environment():
#     """Test if the environment can be created and run"""
#     try:
#         print("Testing environment setup...")
#         env = create_environment()
#         print_environment_info(env)
        
#         # Test a few steps
#         obs = env.reset()
#         print(f"Initial observation shape: {obs.shape}")
        
#         for i in range(3):
#             action = env.action_space.sample()
#             obs, reward, done, info = env.step(action)
#             print(f"Step {i+1}: Action={action}, Reward={reward}, Done={done}")
#             if done:
#                 break
        
#         env.close()
#         print("✅ Environment test passed!")
#         return True
        
#     except Exception as e:
#         # print(f"❌ Environment test failed: {e}")
#         # return False
      
#         import traceback
#         traceback.print_exc() # <-- This will show us the exact line and file crashing
#         print(f"❌ Environment test failed: {e}")
#         return False


# def train_mode(args):
#     """Run training mode"""
#     print("🎯 Starting Training Mode")
#     print("=" * 50)
    
#     # Set random seeds
#     np.random.seed(args.seed)
#     tf.random.set_seed(args.seed)
    
#     # Run training
#     train_main()


# def test_mode(args):
#     """Run testing mode"""
#     print("🧪 Starting Testing Mode")
#     print("=" * 50)
    
#     # Check if weights file exists
#     weights_path = 'dqn_spaceinvaders_weights.h5f'
#     if not os.path.exists(weights_path):
#         print(f"❌ Error: Weights file not found: {weights_path}")
#         print("Please train the agent first using: python main.py --mode train")
#         return
    
#     # Set random seeds
#     np.random.seed(args.seed)
#     tf.random.set_seed(args.seed)
    
#     # Run testing
#     test_main()


# def demo_mode(args):
#     """Run demo mode with visualization"""
#     print("🎮 Starting Demo Mode")
#     print("=" * 50)
    
#     # Check if weights file exists
#     weights_path = 'dqn_spaceinvaders_weights.h5f'
#     if not os.path.exists(weights_path):
#         print(f"❌ Error: Weights file not found: {weights_path}")
#         print("Please train the agent first using: python main.py --mode train")
#         return
    
#     try:
#         from test_agent import load_trained_agent, test_agent_performance
        
#         # Create environment with rendering
#         env = create_environment(render_mode='human')
        
#         # Load trained agent
#         agent = load_trained_agent(weights_path, env)
        
#         # Run demo episodes
#         print("Running demo episodes...")
#         results = test_agent_performance(env, agent, num_episodes=args.episodes, render=True)
        
#         print(f"\nDemo completed! Average reward: {results['mean_reward']:.2f}")
        
#         env.close()
        
#     except Exception as e:
#         print(f"❌ Demo mode failed: {e}")


# def main():
#     """Main entry point"""
#     parser = argparse.ArgumentParser(
#         description="Space Invaders DQN - Deep Reinforcement Learning Project",
#         formatter_class=argparse.RawDescriptionHelpFormatter,
#         epilog="""
# Examples:
#   python main.py --mode train                    # Train the agent
#   python main.py --mode test                     # Test the trained agent
#   python main.py --mode demo --episodes 3        # Run demo with 3 episodes
#   python main.py --mode check                    # Check dependencies and environment
#         """
#     )
    
#     parser.add_argument(
#         '--mode',
#         choices=['train', 'test', 'demo', 'check'],
#         default='check',
#         help='Mode to run: train, test, demo, or check dependencies'
#     )
    
#     parser.add_argument(
#         '--episodes',
#         type=int,
#         default=5,
#         help='Number of episodes for demo mode (default: 5)'
#     )
    
#     parser.add_argument(
#         '--seed',
#         type=int,
#         default=42,
#         help='Random seed for reproducibility (default: 42)'
#     )
    
#     parser.add_argument(
#         '--no-banner',
#         action='store_true',
#         help='Skip printing the banner'
#     )
    
#     args = parser.parse_args()
    
#     # Print banner
#     if not args.no_banner:
#         print_banner()
    
#     # Check dependencies
#     if not check_dependencies():
#         sys.exit(1)
    
#     # Run selected mode
#     try:
#         if args.mode == 'check':
#             print("🔍 Checking environment...")
#             if test_environment():
#                 print("\n✅ All checks passed! Ready to train or test.")
#             else:
#                 print("\n❌ Environment check failed!")
#                 sys.exit(1)
                
#         elif args.mode == 'train':
#             train_mode(args)
            
#         elif args.mode == 'test':
#             test_mode(args)
            
#         elif args.mode == 'demo':
#             demo_mode(args)
            
#     except KeyboardInterrupt:
#         print("\n\n⚠️  Interrupted by user")
#         sys.exit(0)
#     except Exception as e:
#         print(f"\n❌ Error: {e}")
#         sys.exit(1)


# if __name__ == "__main__":
#     main()


"""
Main execution script for Space Invaders DQN Agent
Handles different running modes: check, train, test, and demo
"""

import os
import argparse
import sys
import numpy as np
import tensorflow as tf

# Modern backend compatibility configuration
os.environ["KERAS_BACKEND"] = "tensorflow"
try:
    import tensorflow.keras.config as tfconfig
    tfconfig.enable_unsafe_deserialization()
except Exception:
    pass

from utils import create_environment, print_environment_info, save_episode_gif
from model import create_dqn_model, get_model_summary
from train import create_dqn_agent, evaluate_agent


def print_header(title):
    """Print a styled header section"""
    print("\n" + "═" * 68)
    print(f"║ {title.center(64)} ║")
    print("═" * 68 + "\n")


def test_environment():
    """Verify that packages, gym environments, and array tracking systems are solid"""
    print("🔍 Checking environment...")
    try:
        print("Testing environment setup...")
        env = create_environment()
        print_environment_info(env)
        
        obs = env.reset()
        print(f"Initial observation shape: {obs.shape}")
        
        # Take a sample step
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        print(f"Sample execution step successful! Done flag: {done}")
        
        env.close()
        print("\n✅ Environment validation check passed successfully!")
        return True
    except Exception as e:
        print(f"\n❌ Environment test failed: {str(e)}")
        return False


def run_demo(episodes=5, save_gif=False):
    """Run trained model frames in native interactive game display mode"""
    print_header("🎮 Starting Demo Mode")
    
    weights_path = 'dqn_spaceinvaders_weights.h5f'

    # CHANGE HERE: Set render_mode to 'human' to launch the actual native game window
    env = create_environment(render_mode='human')
    model = create_dqn_model(env.observation_space.shape, env.action_space.n)
    agent = create_dqn_agent(env, model)
    
    print(f"Loading weights from checkpoint base: {weights_path}")
    try:
        agent.load_weights(weights_path)
    except Exception:
        try:
            agent.load_weights('dqn_spaceinvaders_weights')
        except Exception as e:
            print(f"❌ Could not load weights: {e}")
            env.close()
            return
    
    for ep in range(episodes):
        print(f"\nRunning Demo Episode {ep+1}/{episodes}...")
        obs = env.reset()
        done = False
        total_reward = 0
        
        # Force the agent into active operational framework tracking
        agent.training = True
        
        while not done:
            # Let Gymnasium's native pygame system update the window
            env.render()
            
            # Use standard forward tracking, which now natively runs the exploratory policy
            action = agent.forward(obs)
            obs, reward, done, info = env.step(action)
            agent.backward(reward, terminal=done)
            total_reward += reward
            
        print(f"Episode {ep+1} Finished! Total Score Reward: {total_reward}")
            
    env.close()
    print("\n🎮 Demo Run Complete!")


def main():
    parser = argparse.ArgumentParser(description="Space Invaders DQN Controller")
    parser.add_argument(
        '--mode', 
        type=str, 
        default='check', 
        choices=['check', 'train', 'test', 'demo'],
        help='Execution mode pipeline option'
    )
    parser.add_argument('--episodes', type=int, default=5, help='Number of episodes for demo mode runs')
    args = parser.parse_args()

    # Print decorative application header splash screen
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║              🚀 SPACE INVADERS DQN PROJECT 🚀                ║
    ║                                                              ║
    ║         Deep Reinforcement Learning with Keras & TF         ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    print("✅ All required packages are installed!")

    if args.mode == 'check':
        test_environment()
        
    elif args.mode == 'train':
        print_header("🎯 Starting Training Mode")
        from train import main as train_main
        train_main()
        
    elif args.mode == 'test':
        print_header("🧪 Starting Testing Mode")
        weights_path = 'dqn_spaceinvaders_weights.h5f'
        
        env = create_environment()
        model = create_dqn_model(env.observation_space.shape, env.action_space.n)
        agent = create_dqn_agent(env, model)
        
        print(f"Loading weights from checkpoint base: {weights_path}")
        try:
            agent.load_weights(weights_path)
        except Exception:
            try:
                agent.load_weights('dqn_spaceinvaders_weights')
            except Exception as e:
                print(f"❌ Loading failed: {e}")
                env.close()
                sys.exit(1)
        
        evaluate_agent(env, agent, nb_episodes=10)
        env.close()
        
    elif args.mode == 'demo':
        run_demo(episodes=args.episodes)


if __name__ == "__main__":
    main()

