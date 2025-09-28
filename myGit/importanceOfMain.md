Even when working alone, you **do need a `main` branch**. It serves as the official, stable, and definitive version of your project.

-----

## Why You Still Need a `main` Branch

Think of your project like a book you're writing. The `main` branch is the **published, final version**. Other branches are your **rough drafts**. You wouldn't want to experiment with new ideas directly in the final copy.

The `main` branch acts as your:

  * **Single Source of Truth:** It's the one true version of your project. If you ever need to deploy your website or share your code, you use what's on `main`.
  * **Safety Net:** Your `main` branch should always contain a version of your code that **works**. If you're trying a new feature on another branch and everything breaks, you can always return to the stable version on `main`.
  * **Clean History:** It keeps your project history organized. Instead of one long stream of every single change, your `main` branch history can just be a series of major, completed features.

-----

## The Solo Developer Workflow

Using branches, even when you're alone, is a powerful and professional habit. Here's how it works:

1.  Your `main` branch is your stable base.
2.  When you want to work on a new feature (e.g., adding a contact page), you create a new branch from `main`:
    ```bash
    git checkout -b add-contact-page
    ```
3.  You do all your work and make all your commits on this new `add-contact-page` branch. Your `main` branch remains untouched and stable.
4.  Once the contact page is finished and working perfectly, you switch back to `main` and merge your changes into it:
    ```bash
    # Switch back to the main branch
    git checkout main

    # Merge the new feature into main
    git merge add-contact-page

    # Push the updated main branch to GitHub
    git push origin main
    ```

This workflow keeps your project clean, safe, and organized.